def expert_Sys(time_free, mood, homeWork, personality, weather, budget, place):
    # Không có thời gian rảnh
    if time_free == '2':
        return "Hiện tại bạn không có thời gian rảnh, hãy làm xong công việc hiện tại để tiếp tục!"

    # có thời gian rảnh nhưng không nhưng tâm trạng lại tệ
    if mood == '3':
        return "Bạn đang mệt, hãy dành thời gian này để nghỉ ngơi trc đã"

    # Ưu tiên bài tập
    if homeWork == '1':
        return "Bạn hãy ưu tiên làm bài tập về nhà trước!"

    # Các recommendation dựa trên mood, personality, weather, budget, and place
    # Vui
    if mood == '1': 
        if personality == '1': # Sôi động
            if weather in ['1', '2']:  # mát or nóng
                if budget in ['1', '2'] and place == '1':  # tiền nhiều, đủ sài
                    return "Đi đánh golf, ý tường không tồi đâu!"
                elif budget in ['1', '2'] and place == '3':  # tiền nhiều nhưng thích mấy nơi sôi động
                    return "hãy rủ bạn bè đi karaoke cao cấp, club hoặc khu vui chơi giải trí lớn :)"
                else:  # tiền hông có, thích những nơi đơn giản
                    return "Hãy đi dạo công viên"
            else:  # mưa, lạnh
                if budget == '1' and place == '1':
                    return "Hãy thử đến một phòng gym cao cấp hoặc một quán cà phê sang trọng."
                else:
                    return "Hãy tham gia một lớp học thể thao trong nhà hoặc gặp gỡ bạn bè ở quán quen để tám chuyện."
        elif personality == '2':  # trầm tính
            if budget == '1' and place == '1':
                return "Bạn thử đến một nhà hàng sang trọng hoặc một spa để thư giãn."
            else:
                return "Ở nhà đọc sách, nghe nhạc hoặc xem một bộ phim nào đó mà bạn cảm thấy thú vị."
        elif personality == '3':  # Sáng tạo
            if budget != '3':
                return "đầu tư mua dụng cụ vẽ, nhạc cụ, tham gia workshop nghệ thuật, hoặc làm một project cá nhân nào đó"
            else:
                return "Thử sáng tạo với các hoạt động miễn phí như viết nhật ký hoặc vẽ bằng vật liệu sẵn có."
        else:  # chăm chỉ
            if place == '3':
                return "Hãy tham gia một workshop hoặc câu lạc bộ để vừa học vừa giao lưu."
            else:
                return "Hãy học một kỹ năng mới hoặc đọc sách chuyên ngành để phát triển bản thân."
    # Buồn       
    if mood == '2':
        if personality in ['2', '3']:  
            if weather in ['3', '4']:  
                return "Tâm trạng bạn không tốt, hãy ở nhà xem phim, đọc sách hoặc nghe nhạc để thư giãn."
            else:
                return "Hãy đi dạo nhẹ nhàng ở công viên hoặc thử thiền để cải thiện tâm trạng."
        elif personality == '1': 
            if weather in ['1', '2']:  
                return "Hãy ra ngoài chạy bộ hoặc gặp bạn bè để khuây khỏa."
            else:
                return "Hãy thử một hoạt động trong nhà như nhảy hoặc xem một bộ phim hài."
        else:  
            return "Hãy tập trung vào một việc nhỏ như đọc sách hoặc sắp xếp lại không gian để cảm thấy tốt hơn."

    # Trường hợp dự phòng nếu thiếu
    return "Hãy thử một hoạt động nhẹ nhàng như đi dạo, nghe nhạc, hoặc trò chuyện với bạn bè."

try:
    time_free = input("Bạn hiện tại có nhiều thời gian rảnh không? (1.Có / 2.Không có): ").strip()
    mood = input("Tâm trạng hiện tại của bạn thế nào? (1.Vui vẻ / 2.Buồn / 3.Mệt mỏi): ").strip()
    homeWork = input("Bạn có bài tập về nhà không? (1.Có / 2.Không): ").strip()
    personality = input("Bạn là một người như thế nào? (1.Năng động / 2.Trầm tính / 3.Sáng tạo / 4.Chăm chỉ): ").strip()
    weather = input("Thời tiết hôm nay thế nào? (1.Mát mẻ / 2.Nóng / 3.Mưa / 4.Lạnh): ").strip()
    budget = input("Bạn có nhiều tiền không? (1.Nhiều / 2.Đủ dùng / 3.Ít): ").strip()
    place = input("Bạn thích một nơi như thế nào? (1.Sang trọng / 2.Đơn giản / 3.Sôi động): ").strip()

    print("{0} Recommending {0}".format('='*30))
    result = expert_Sys(time_free, mood, homeWork, personality, weather, budget, place)
    print(result)

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại!")