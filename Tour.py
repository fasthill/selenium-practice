# 상품정보를 담는 클래스
class TourInfo:
    # 멤버 변수 (실제 컴럼 보다는 적게 생성했음)
    title = ''
    price = ''
    area = ''
    link = ''
    img = ''
    # 생성자
    def __init__(self, title, price, area, link, img):
        self.title = title
        self.price = price
        self.area = area
        self.link = link
        self.img = img