# -*- coding: utf-8 -*-

import requests

def test_chat():
    artifact_name = '莲鹤方壶'
    # 发送音频
    file_path = "RAG\\audio\\hello.wav"
    with open(file_path, "rb") as file:
        response = requests.post(
            f"http://localhost:10004/aichat/{artifact_name}", 
            files={"audio": ('hello.wav', file.read(), 'audio/wav')}
        )
        print(response.text)

def test_update_db():
    texts = ['明黄色缎地平金银彩绣五毒活计，清同治，清宫旧藏。清代满族习俗，特别喜爱在腰带或领襟之间的钮扣上佩挂各类日常随手可用的小杂品，如荷包、扇套、表套、搬指套、香囊、眼镜盒、褡裢、槟榔袋、钥匙袋、靴掖等，通称“活计”。这些活计既很实用，装饰性也很强，并往往根据节庆时令的变化而佩挂纹样形制不同的活计。这套活计是端午节佩戴之物，共9件，其中荷包3件、烟荷包1件、表套1件、扇套1件、镜子1件、粉盒1件、名姓片套1件。每件的颜色和纹样相同，均为明黄色，通体以金线、银线和五彩丝线绣五毒和“大吉”葫芦纹。“五毒”为蛇、蟾蜍、蝎子、壁虎和蜈蚣五种有毒动物，配以“大吉”字样和葫芦纹样相组合，寓意以毒攻毒，以恶镇恶，驱邪免灾。整套活计用色明快华丽，纹样生动逼真，绣工精美细巧，为佩挂者平添仪态之美，同时也寄托了佩挂者希冀籍此避邪趋吉的美好愿望。']
    collection = 'test_collection'
    response = requests.post(
        f"http://localhost:10004/update_db?texts={texts}&collection_name={collection}"
    )
    print(response.text)

if __name__ == '__main__':
    # test_chat()
    test_update_db()