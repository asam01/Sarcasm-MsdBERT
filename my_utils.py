import shutil

def make_toy_images(data, img_dir, filename, k):

    counter = 0
    lines = []
    for line in data:

        print(counter)

        tweet_id = eval(line)[0]
        # print("src path: ", img_dir+"/"+tweet_id+".jpg")
        try:
            shutil.copy(img_dir+"/"+tweet_id+".jpg", "toy_images")
            lines.append(line)

            counter +=1
            if counter == k:
                f_toy = open("toy_data/"+filename+".txt", "w")
                f_toy.writelines(lines)
                f_toy.close()
                break
        except:
            print(tweet_id)
            continue

def make_toy_dataset(k, img_dir): #k = size of toy dataset, img_dir = directory where u already have the images

    filenames = ["train", "test", "valid"]
    for filename in filenames:
        f_in = open("data/"+filename+".txt", "r")
        data = f_in.readlines()
        f_in.close()
    
        make_toy_images(data, img_dir, filename, k)


make_toy_dataset(10, "/projects/tir3/users/nnishika/data-of-multimodal-sarcasm-detection/dataset_image")



