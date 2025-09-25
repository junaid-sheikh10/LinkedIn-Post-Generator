import json


def process_post(raw_file_path,processed_file_path="Data/processed_posts.json"):
    print("processing")
    enriched_posts=[] 
    with open(raw_file_path,'r', encoding= 'utf-8') as file:
        posts=json.load(file)
        for post in posts:
            metadata=extract_metadata(post['text'])
            post_with_metadata= post | metadata
            enriched_posts.append(post_with_metadata)
    
    for epost in enriched_posts:
        print(epost)

def extract_metadata(post):
    return{
        'line_count':10,
        'language':"English",
    }

if __name__ == "__main__":
    process_post("Data/raw_posts.json","Data/processed_posts.json")