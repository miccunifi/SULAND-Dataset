import os

# Update this path as per your directory structure
dataset_dir = f"data-ood/val/labels"

def count_non_empty_files(directory):
    count_per_video = {}
    for video_folder in os.listdir(directory):
        video_folder_path = os.path.join(directory, video_folder)
        if os.path.isdir(video_folder_path):
            non_empty_files = 0
            for file in os.listdir(video_folder_path):
                if file.endswith(".txt"):
                    file_path = os.path.join(video_folder_path, file)
                    if os.path.getsize(file_path) > 0:  # Check if file is not empty
                        non_empty_files += 1
            count_per_video[video_folder] = non_empty_files
    return count_per_video

# Count non-empty .txt files in each video subfolder
non_empty_file_counts = count_non_empty_files(dataset_dir)
print(non_empty_file_counts)
