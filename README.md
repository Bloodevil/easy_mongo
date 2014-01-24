easy_mongo
==========
사용법

server form : 몽고 데이터베이스 서버이름 입력. 깔려있는곳과 동일하면 localhost
db form : 보고싶은 db -> 추후 서버에 붙고나면 디비 리스트가 나오도록 변경할 예정.(최초 1회 접속 필요)
collection form : 보고싶은 collection -> 서버에 붙고나면 컬렉션 리스트가 나오도록 변경할 예정. (최초 1회 접속 필요)

query form : 현재는 find query form만 지원. 아무것도 안쓰면 db.collection.find() 를 했을때와 동일한 결과.
             뭔가 쓰게되면 db.collection.find(query) 이런 식으로 들어가게 된다.
             find 이외에 count ... 귀찮아서 쓰지 못한 많은 것들을 지원할 예정. (주로 내가 쓸 것들. aggregate 라든가..)


mongo terminal이 이것저것 먹어서 (한글도 먹고.. 등등)만듬. 

require
==========
 : flask
 : pymongo
 
 
