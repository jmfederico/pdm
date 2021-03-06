import argparse
import shutil

from pdm.cli.commands.base import BaseCommand
from pdm.cli.options import verbose_option
from pdm.iostream import stream
from pdm.project import Project


class Command(BaseCommand):
    """Display the current configuration"""

    arguments = [verbose_option]

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers()
        ClearCommand.register_to(subparsers, "clear")

    def handle(self, project: Project, options: argparse.Namespace) -> None:
        pass


class ClearCommand(BaseCommand):
    """Show a configuration value"""

    arguments = [verbose_option]

    def handle(self, project: Project, options: argparse.Namespace) -> None:
        shutil.rmtree(project.cache_dir, ignore_errors=True)
        stream.echo("Caches are cleared successfully.")
