import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # 1. Get the absolute path of the allowed working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # 2. Safely join and normalize the target directory path
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # 3. Check if the target directory actually falls within the working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        # 4. Check if the verified path is an actual directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
            
        # 5. Read directory contents and compile size/type info
        items = os.listdir(target_dir)
        lines = []
        for item in items:
            item_path = os.path.join(target_dir, item)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)
            lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            
        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"
