import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # 1. Path safety and normalization guardrails
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Guardrail: Ensure path is strictly inside the working directory
        if os.path.commonpath([working_dir_abs, target_file_path]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        # Guardrail: Prevent overwriting an actual directory folder
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
            
        # 2. Extract parent tree path and build missing folders automatically
        parent_dir = os.path.dirname(target_file_path)
        os.makedirs(parent_dir, exist_ok=True)
        
        # 3. Write/overwrite file content
        with open(target_file_path, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"
