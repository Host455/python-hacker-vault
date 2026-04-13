import re

def detect_intrusion(log_file_path):
    suspicious_patterns = {
        'Brute force detected (Failed password)': r'Failed password',
        'SQL injection (Invalid user)': r'Invalid user',
        'XSS scripting (Authentication failure)': r'authentication failure',
        'Accepted password for invalid user': r'Accepted password for invalid user'
    }
    
    detailed_feedback = []
    total_suspicious_activities = 0
    
    try:
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
        
        for description, pattern in suspicious_patterns.items():
            matches = re.findall(pattern, log_content)
            if matches:
                total_suspicious_activities += len(matches)
                detailed_feedback.append(f"{description}: {len(matches)} occurrences")
    except FileNotFoundError:
        return False, [], 0
    
    intrusion_detected = total_suspicious_activities >= 10
    return intrusion_detected, detailed_feedback, total_suspicious_activities
