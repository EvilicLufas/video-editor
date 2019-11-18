'''
This function gives you the possibility to 
split videos into multiple parts.

TODO Fix OSError: [WinError 6] The handle is invalid.
'''

import moviepy.editor as mp

def create_split():
    # Give user the option to split the video into multiple parts.

    file_path = input('Enter path to file: ')
    video_parts = int(input('Enter amount of video parts: '))

    # Used to rename the video parts (removes everything before the last forwardslash)
    index= file_path.rsplit('\\', 1)[-1]   

    # Calculate the total time of each video part.
    video = (mp.VideoFileClip(file_path))
    time_per_part = video.duration / video_parts

    # Store the begin and end time of each video part
    part_duration = 0
    start_time = [0]
    end_time = []

    # This loop appends the total time of each video part to the start_time and end_time array
    for _ in range(int(video_parts)):
        part_duration += time_per_part
        start_time.append(round(part_duration, 2))
        end_time.append(round(part_duration, 2))

    # the last value in the start_time array gets deleted because it's only needed for the end_time array
    del start_time[-1]

    # Give each video part a start and end time with the values that are stored in their arrays
    for part in range(int(video_parts)):
        new_filename = f'part-{part}-{index}'

        # video = (mp.VideoFileClip(file_path)
        #         .subclip((start_time[int(part)]), (end_time[int(part)])))
        # video.write_videofile(new_filename)

        # close the video to prevent 'OSError: [WinError 6] The handle is invalid'
        # video.reader.close()
        # video.audio.reader.close_proc()
