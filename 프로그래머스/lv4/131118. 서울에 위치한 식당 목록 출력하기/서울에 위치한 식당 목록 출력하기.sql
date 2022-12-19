-- 코드를 입력하세요
SELECT A.rest_id, A.rest_name, A.food_type, A.favorites, A.address, round(Avg(B.review_score),2) AS average 
FROM rest_info A
    INNER JOIN rest_review B ON A.rest_id = B.rest_id 
WHERE a.address LIKE '서울%'
GROUP BY A.rest_id, A.rest_name, A.food_type, A.favorites, A.address
ORDER BY average DESC, A.favorites DESC