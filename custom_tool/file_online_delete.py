import requests
import base64
import os
from datetime import datetime


class FileOnlineDelete_gitee:
    def __init__(self):
        self.url_prefix = 'https://gitee.com/api/v5/repos/'
        self.show_help = "placeholder"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "repo_owner": ("STRING", {}),
                "repo_name": ("STRING", {}),
                "access_token": ("STRING", {}),
                "branch": ("STRING",{}),
                "file_path": ("STRING", {})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("show_help",)

    FUNCTION = "delete_file_from_branch"
    CATEGORY = "大模型派对（llm_party）/函数（function）"

    def delete_file_from_branch(
        self,
        repo_owner, 
        repo_name, 
        file_path, 
        branch, 
        access_token,
        commit_message = "[comfyui_LLM_party] file deleted"):

        url = f"https://gitee.com/api/v5/repos/{repo_owner}/{repo_name}/contents/{file_path}"

        params = {
            "access_token": access_token,
            "ref": branch
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Failed to get file info. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False

        file_sha = response.json()['sha']

        data = {
            "access_token": access_token,
            "message": commit_message,
            "sha": file_sha,
            "branch": branch
        }
        response = requests.delete(url, json=data)

        if response.status_code == 200:
            print(f"File '{file_path}' successfully deleted from branch '{branch}'.")
            return ("Success", )
        else:
            print(f"Failed to delete file. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return (response.text, )


NODE_CLASS_MAPPINGS = {
    "FileOnlineDelete_gitee": FileOnlineDelete_gitee,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "FileOnlineDelete_gitee": "清理Gitee文件床🐶（FileOnlineDelete_gitee）",
}

if __name__=="__main__":
    file_path="image.jpg"
    obj = FileOnlineDelete_gitee()
    obj.delete_file_from_branch(
        repo_owner="comfyui_LLM_party", 
        repo_name="comfyui_LLM_party", 
        branch="comfyui_LLM_party",
        file_path=file_path, 
        access_token="comfyui_LLM_party")