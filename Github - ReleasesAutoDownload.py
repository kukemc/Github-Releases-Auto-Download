import requests
import json

def download_releases(owner, repo, keywords):
    # 构建 API URL
    # Build the API URL
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"

    # 发送 GET 请求获取所有 Releases 的信息
    # Send a GET request to fetch all the Releases information
    response = requests.get(url)
    releases = json.loads(response.text)

    # 遍历每个 Release
    # Iterate over each Release
    for release in releases:
        # 检查是否包含关键词
        # Check if it contains any of the keywords
        if any(keyword in release["name"] for keyword in keywords):
            # 遍历每个 Asset
            # Iterate over each Asset
            for asset in release["assets"]:
                asset_name = asset["name"]
                asset_url = asset["browser_download_url"]
                # 下载文件
                # Download the file
                print(f"Downloading {asset_name}...")
                response = requests.get(asset_url)
                with open(asset_name, "wb") as file:
                    file.write(response.content)

# 输入参数
# Input parameters
owner = "SIPC"
repo = "Releases-Auto-Download"
keywords = ["v"]

# 调用下载函数
# Call the download function
download_releases(owner, repo, keywords)