# 공과 벽돌 또는 패들간의 충돌 감지
# 충돌 검사
# 충돌 시 처리 관련 메서드


def detect_collision(ball, paddle, bricks):
    # 공이 패들과 충돌하는지 확인
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1


    # 공이 벽돌과 충돌하는지 확인
    for brick in bricks:
        if not brick.hidden and ball.rect.colliderect(brick.rect):
            brick.hidden = True
            ball.speed_y *= -1
            return True


    return False