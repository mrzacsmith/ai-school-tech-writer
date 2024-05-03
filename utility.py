import os
import base64
from openai import OpenAI


def format_data_for_openai(diffs, readme_content, commit_messages):
    prompt = None

    # Combine the changes into a string with clear delineation.
    changes = "\n".join([])

    # Combine all commit messages
    commit_messages = "\n".join(commit_messages) + '\n\n'
    # Decode the README content

    # Construct the prompt with clear instructions for the LLM.
    prompt = (
        "Please review the following code changes and commit messages from a GitHub pull request:\n"
        "Code changes from Pull Request:\n"
        f"{changes}\n"
        "Commit messages:\n"
        f"{commit_messages}"
        "Here is the current README file content:\n"
        f"{readme_content}\n"
        "Consider the code changes and commit messages, determine if the README needs to be updated. If so, edit the README, ensuring to maintain its existing style and clarity.\n"
        "Updated README:\n"
    )
    return prompt


def call_openai(prompt):
    pass


def update_readme_and_create_pr(repo, updated_readme, readme_sha):
    pass
