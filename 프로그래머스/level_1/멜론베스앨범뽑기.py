def get_melon_best_album(genre_array, play_array):
    info_list = []
    song_kind = dict.fromkeys(set(genre_array), [])

    for i in range(len(genre_array)):
        info_list.append((play_array[i], genre_array[i], i))
    info_list.sort(reverse=True)

    for info in info_list:
        song_kind[info[1]].append(info)
        print(info)
        print(info[1])
        print(song_kind[info[1]])
        print(song_kind)


    print(song_kind)
    return []


if __name__ == '__main__':
    print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
          get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
    print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
          get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
                               [2000, 500, 600, 150, 800, 2500, 2000]))
