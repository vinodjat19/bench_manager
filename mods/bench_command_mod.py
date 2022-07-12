import frappe, os, json
from subprocess import PIPE, STDOUT, Popen, check_output

@frappe.whitelist()
def console_command(doc, key, caller, branch_name=None, remote=None, commit_msg=None):
    doc = json.loads(doc)
    cwd = os.path.join("..", "apps", doc.get("name"))
    remote = check_output("git remote".split(), cwd=cwd).decode().strip("\n")
    commands = {
        "push": [
            "git push {remote} {branch_name}".format(
					branch_name=doc.get("current_git_branch"), remote=remote
				)
        ]
    }
    frappe.enqueue(
        "bench_manager.bench_manager.utils.run_command",
        commands=commands[caller],
        cwd=cwd,
        doctype=doc.get("doctype"),
        key=key,
        docname=doc.get("name"),
    )