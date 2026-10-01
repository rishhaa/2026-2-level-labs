"""
Language detection starter.
"""

# pylint: disable=unused-variable, duplicate-code
from lab_1_classify_profile.main import create_language_profile, detect_language_by_mse, calculate_mse, calculate_rmse


def main() -> None:
    """
    Launches an implementation.
    """
    with open("lab_1_classify_profile/assets/texts/de.txt", "r", encoding="utf-8") as file:
        de_text = file.read()
    with open("lab_1_classify_profile/assets/texts/unknown.txt", "r", encoding="utf-8") as file:
        unknown_text = file.read()
    with open("lab_1_classify_profile/assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    with open("lab_1_classify_profile/assets/texts/en.txt", "r", encoding="utf-8") as file:
        en_text = file.read()
    if en_profile and de_profile and unknown_profile:
        # ... тут твой остальной код ...

        # Демонстрация для защиты на реальных текстах
        mse_en = compare_profiles_by_mse(unknown_profile, en_profile)
        mse_de = compare_profiles_by_mse(unknown_profile, de_profile)

        if mse_en is not None and mse_de is not None:
            print("\n--- Сравнение метрик на реальных текстах ---")
            print(f"С неизвестного на Английский -> MSE: {mse_en:.5f} | RMSE: {mse_en ** 0.5:.5f}")
            print(f"С неизвестного на Немецкий   -> MSE: {mse_de:.5f} | RMSE: {mse_de ** 0.5:.5f}")
    test_pred = [0.2, 0.5, 0.1]
    test_actual = [0.1, 0.5, 0.4]
    print("Сравнение работы метрик на одинаковых текстах:")
    print(f"Результат MSE: {calculate_mse(test_pred, test_actual)}")
    print(f"Результат RMSE: {calculate_rmse(test_pred, test_actual)}")
    result = None
    en_profile = create_language_profile("en", en_text, stopwords)
    de_profile = create_language_profile("de", de_text, stopwords)
    unknown_profile = create_language_profile("unknown", unknown_text, stopwords)

    if en_profile and de_profile and unknown_profile:
        result = detect_language_by_mse(unknown_profile, en_profile, de_profile)
    assert result, "Detection result is None"
    print(result)



if __name__ == "__main__":
    main()
