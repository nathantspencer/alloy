import subprocess

print('Watching scss directory for changes...')
subprocess.check_output(['sass','--watch', 'static/scss/:static/css/'])