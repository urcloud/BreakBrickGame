def detect_collision(ball, paddle, bricks):
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1

    for brick in bricks:
        if brick.durability > 0 and ball.rect.colliderect(brick.rect):
            if brick.hit():
                bricks.remove(brick)
            ball.speed_y *= -1
            return True
    return False
