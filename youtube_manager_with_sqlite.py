import sqlite3

conn = sqlite3.connect('youtube_manager.db')

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )              
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("EMPTY ROW")
    else:
        for row in rows:
            print("*" * 70)
            print(row)
        print("*" * 70)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()


def update_a_video_list(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(video_id,new_name,new_time))
    conn.commit()

def delete_a_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()




def main():
    while True:
        print('\n Youtube Manager App with DB| choose the Option please')
        print('1.List all videos')
        print('2.Add a video')
        print('3.Update a videos list')
        print('4.Delete a video from the list')
        print('5.Close the app')
        choice = input('Choose the given options from the list : ')
        


        if choice == '1':
            list_all_videos()
        
        elif choice == '2':
            input("Enter Video ID to add: ")
            name = input('Enter the Video name : ')
            time = input('Enter video time: ')
            add_video(name,time)
        
        elif choice == '3':
            video_id = input("Enter Video ID to Update : ")
            name = input('Enter the Video name : ')
            time = input('Enter video time: ')
            update_a_video_list(video_id,name,time)
        
        elif choice == '4':
            video_id = input("Enter Video ID to remove : ")
            delete_a_video(video_id)
        
        elif choice == '5':
            break
        
        else:
            print('Invalid Input')

    conn.close
if __name__ == '__main__':
    main()