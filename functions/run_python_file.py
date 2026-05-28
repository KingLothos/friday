import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        # 1. Path safety and containment validation
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        if os.path.commonpath([working_dir_abs, absolute_file_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        # 2. File verification checks
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
            
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
            
        # 3. Assemble the runtime command array
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)
            
        # 4. Spawning the process safely
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            text=True,
            capture_output=True,
            timeout=30
        )
        
        # 5. Format stdout, stderr, and exit code conditions
        output_lines = []
        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")
            
        if not result.stdout.strip() and not result.stderr.strip():
            output_lines.append("No output produced")
        else:
            if result.stdout:
                output_lines.append(f"STDOUT:\n{result.stdout.strip()}")
            if result.stderr:
                output_lines.append(f"STDERR:\n{result.stderr.strip()}")
                
        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"
