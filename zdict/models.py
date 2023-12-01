from django.db import models


class TaiwanChineseDict(models.Model):
    id = models.IntegerField(primary_key=True)
    term_name = models.TextField()
    term_alias = models.TextField()
    char_nums = models.TextField()
    char_no = models.TextField()
    radical_char = models.TextField()
    stroke_nums = models.TextField()
    stroke_nums_except_radical_char = models.TextField()
    polyphonic_sorting = models.TextField()
    zhuyin_yishi = models.TextField()
    variant_type = models.TextField()
    variant_zhuyin = models.TextField()
    hanyu_pinyin = models.TextField()
    variant_hanyu_pinyn = models.TextField()
    similar_words = models.TextField()
    opposite_words = models.TextField()
    interpretation = models.TextField()
    multi_phonetic_see_msg = models.TextField()
    various_char = models.TextField()

    def __str__(self):
        result = []
        result.append(self.id)
        result.append(self.term_name)
        result.append(self.term_alias)
        result.append(self.char_nums)
        result.append(self.char_no)
        result.append(self.radical_char)
        result.append(self.stroke_nums)
        result.append(self.stroke_nums_except_radical_char)
        result.append(self.polyphonic_sorting)
        result.append(self.zhuyin_yishi)
        result.append(self.variant_type)
        result.append(self.variant_zhuyin)
        result.append(self.hanyu_pinyin)
        result.append(self.variant_hanyu_pinyn)
        result.append(self.similar_words)
        result.append(self.opposite_words)
        result.append(self.interpretation)
        result.append(self.multi_phonetic_see_msg)
        result.append(self.various_char)
        return str(result)

    class Meta:
        managed = False
        db_table = 'taiwan_chinese_dict'
