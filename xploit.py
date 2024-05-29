import requests

def check_vulnerabilities(url):
    try:
        
        response = requests.get(url)
        print(f"Status code: {response.status_code}")

       
        open_directories = ['/admin', '/backup', '/config', '/logs', '/temp', '/tmp', '/test', '/testing', '/upload', '/uploads', '/public', '/public_html', '/scripts', '/vendor']
        
       
        for directory in open_directories:
            directory_url = url + directory
            response = requests.get(directory_url)
            if response.status_code == 200:
                print(f"Potential open directory found: {directory_url}")

    except requests.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    target_url = "URL"  # input the url of website you want to perform attack.
    check_vulnerabilities(target_url)
