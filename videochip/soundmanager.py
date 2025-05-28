import os
import mido


def CheckingSizelimits(filepathCheck):
    filesizebytesCheck = os.path.getsize(filepathCheck)
    print(f"File size (bytes): {filesizebytesCheck}")
    if filesizebytesCheck > 250000:
        print("File size exceeds 250KB, please reduce the file size.")
        return False
    else:
        return True
def compressor(fielpath):
    if CheckingSizelimits(fielpath):
        print("there is no need to compress the file, it is under 250KB")
    else: 
        midiEdit = mido.MidiFile(fielpath)
        cutofftimeCompression = 57600
        for track in midiEdit.tracks:
            print(track.name)
            for channel in track.channels:
                print(channel.name)
                # for each channel in the track
                messages_to_remove = []
            # creates a list of messages to get rid of
                for msg in channel:
                    print(msg)
                    # for each message/note in the track
                    if msg.type == 'note_on' or msg.type == 'note_off':
                        # if the message is a note on or note off
                        if msg.time > cutofftimeCompression:
                            # if the time of the message is greater than the cutoff time
                            messages_to_remove.append(msg)
                            print("messages to remove: ", messages_to_remove)
            # after the loop, remove the messages that are in the list
                for msg in messages_to_remove:
                    channel.remove(msg)
        midiEdit.save('Compressed.mid')


compressor(r"C:\Users\adena\OneDrive\Desktop\Pyth-M20\systemfiles\BeepBox-Song.mid")
