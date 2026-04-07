
logs = []

def log_request(path, status):
    logs.append({
        "path": path,
        "status": status
    })

def get_logs():
    return logs
