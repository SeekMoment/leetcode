class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) != 0:
            return -1
        elif len(haystack) == 0 or len(needle) == 0:
            return 0
        S = set()  # уникальные символы в образе
        M = len(needle)  # число символов в образе
        d = {}  # словарь смещений

        for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
            if needle[i] not in S:  # если символ еще не добавлен в таблицу
                d[needle[i]] = M - i - 1
                S.add(needle[i])

        if needle[M - 1] not in S:  # отдельно формируем последний символ
            d[needle[M - 1]] = M

        d['*'] = M  # смещения для прочих символов

        # Этап 2: поиск образа в строке

        N = len(haystack)

        if N >= M:
            i = M - 1  # счетчик проверяемого символа в строке

            while (i < N):
                k = 0
                j = 0
                flBreak = False
                for j in range(M - 1, -1, -1):
                    if haystack[i - k] != needle[j]:
                        if j == M - 1:
                            off = d[haystack[i]] if d.get(haystack[i], False) else d[
                                '*']  # смещение, если не равен последний символ образа
                        else:
                            off = d[needle[j]]  # смещение, если не равен не последний символ образа

                        i += off  # смещение счетчика строки
                        flBreak = True  # если несовпадение символа, то flBreak = True
                        break

                    k += 1  # смещение для сравниваемого символа в строке

                if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
                    return i - k + 1
            else:
                return -1
        else:
            return -1
