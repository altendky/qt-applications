import pathlib
import subprocess


completed_process = subprocess.run(
    ['ldconfig', '-p'],
    check=True,
    stdout=subprocess.PIPE,
    encoding='utf-8',
)

print(completed_process.stdout)

[xcb_util_line] = [
    line
    for line in completed_process.stdout.splitlines()
    if 'libxcb-util' in line
]

existing_xcb_util_path = pathlib.Path(xcb_util_line.split('=>')[1])
new = existing_xcb_util_path.with_suffix('.0')
new.symlink_to(existing)

