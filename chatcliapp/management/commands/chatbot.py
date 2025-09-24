"""
Usage:
    python manage.py chatbot              # run the REPL
    python manage.py chatbot --train      # train on English corpus, then run
    python manage.py chatbot --reset      # wipe the bot's SQLite DB before running

Author: Minh Le
"""
import os
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

# ChatterBot imports
try:
    # Works for chatterbot2 (modern fork)
    from chatterbot import ChatBot
    from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
except Exception as exc:
    raise CommandError(
        "ChatterBot is not installed or incompatible with your Python version. "
        "Try installing either 'chatterbot==1.0.4' (Py<=3.8) or 'chatterbot2' (Py>=3.9)."
    ) from exc


class Command(BaseCommand):
    help = "Open a terminal chat session with a ChatterBot instance."

    def add_arguments(self, parser):
        parser.add_argument(
            "--train",
            action="store_true",
            help="Train on the default English corpus before starting the chat.",
        )
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete the bot's SQLite database before starting.",
        )

    def handle(self, *args, **options):
        project_root = Path(__file__).resolve().parents[4]  # repo root
        db_path = project_root / "chatterbot.sqlite3"

        if options["reset"] and db_path.exists():
            db_path.unlink()
            self.stdout.write(self.style.WARNING("Removed chatterbot.sqlite3"))

        # Configure the ChatBot instance.
        # We use SQLStorageAdapter with a local SQLite DB file.
        # BestMatch is the simplest logic adapter for quick demos.
        bot = ChatBot(
            "TerminalBot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri=f"sqlite:///{db_path}",
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    # Optionally tweak response selection/training parameters:
                    # "maximum_similarity_threshold": 0.90,
                }
            ],
            read_only=False,  # allow learning during list training
        )

        if options["train"]:
            self.stdout.write(self.style.NOTICE("Training on English corpus..."))
            trainer = ChatterBotCorpusTrainer(bot)
            # e.g. 'chatterbot.corpus.english.greetings', 'conversations'
            trainer.train("chatterbot.corpus.english")

            # Add a few domain-specific examples to improve the sample I/O in the prompt:
            list_trainer = ListTrainer(bot)
            list_trainer.train(
                [
                    "Hello! How are you doing?",
                    "I am doing very well, thank you for asking.",
                    "Who made you?", 
                    "I was created for a class assignment using Django and ChatterBot.",
                    "What can you do?", 
                    "I can chat in the terminal and learn from examples.",
                    "Thanks!", 
                    "You're welcome!",
                ]
            )
            self.stdout.write(self.style.SUCCESS("Training complete."))

        self.stdout.write(self.style.SUCCESS("Chat ready. Type 'exit' or 'quit' to leave.\n"))

        # Simple terminal REPL
        try:
            while True:
                user_text = input("you: ").strip()
                if user_text.lower() in {"exit", "quit"}:
                    print("bot: Bye! 👋")
                    break

                if not user_text:
                    continue

                try:
                    reply = bot.get_response(user_text)
                except Exception as exc:
                    self.stderr.write(self.style.ERROR(f"Error generating response: {exc}"))
                    continue

                print(f"bot: {reply}")
        except KeyboardInterrupt:
            print("\nbot: Bye! 👋")
