import os

def get_file_content(working_directory: str, file_path: str) -> str:
    MAX_CHARS = 10000
    try:
        # 1. Target directory security checks
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Guardrail: Ensure file is inside working directory
        if os.path.commonpath([working_dir_abs, target_file_path]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        # Guardrail: Ensure it is an actual, existing regular file
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
            
        # 2. Read file contents up to the maximum limit
        with open(target_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            
            # Check if there is more content left over after the first chunk
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
        return content

    except Exception as e:
        return f"Error: {str(e)}"
