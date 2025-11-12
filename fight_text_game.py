import random
import time

print("⚔️ GAME CHIẾN ĐẤU CHỮ ⚔️")
print("Bạn là chiến binh dũng cảm! Một con quái vật xuất hiện!\n")

player_hp = 100
enemy_hp = 80
turn = 1

while player_hp > 0 and enemy_hp > 0:
    print(f"\n--- Lượt {turn} ---")
    print(f"Máu bạn: {player_hp} ❤️ | Máu quái vật: {enemy_hp} 👹")
    print("1. Tấn công ⚔️")
    print("2. Phòng thủ 🛡️")
    print("3. Hồi máu 💊")

    choice = input("Chọn hành động (1-3): ")

    if choice == "1":
        dmg = random.randint(15, 25)
        enemy_hp -= dmg
        print(f"💥 Bạn tấn công gây {dmg} sát thương!")
    elif choice == "2":
        print("🛡️ Bạn phòng thủ, giảm sát thương lượt này!")
    elif choice == "3":
        heal = random.randint(10, 20)
        player_hp += heal
        if player_hp > 100:
            player_hp = 100
        print(f"💊 Bạn hồi {heal} máu!")
    else:
        print("❌ Lựa chọn không hợp lệ!")
        continue

    time.sleep(1)
    # Quái vật phản công
    if enemy_hp > 0:
        enemy_action = random.choice(["attack", "attack", "miss"])
        if enemy_action == "attack":
            enemy_dmg = random.randint(10, 20)
            if choice == "2":  # nếu phòng thủ, giảm sát thương
                enemy_dmg //= 2
            player_hp -= enemy_dmg
            print(f"👹 Quái vật tấn công gây {enemy_dmg} sát thương!")
        else:
            print("😈 Quái vật tấn công hụt!")

    turn += 1
    time.sleep(1)

if player_hp <= 0 and enemy_hp <= 0:
    print("\n⚔️ Cả hai cùng gục ngã... hòa!")
elif enemy_hp <= 0:
    print("\n🏆 Bạn đã chiến thắng con quái vật!")
else:
    print("\n💀 Bạn đã bị đánh bại...")
