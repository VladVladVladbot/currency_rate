currency = (
    (2.56, "BYN"),
    (63.76, "RUB"),
    (1.03, "EUR"),
    (36.85, "UAN"),
    (146.85, "JPY"),
    (1, 'USD'),
)


class Translate:
    def translate(self, cleaned_data, context):
        count = cleaned_data['count']
        count_1 = cleaned_data['count_1']
        count_2 = cleaned_data['count_2']
        last_count = round(float(count_2) / float(count_1) * count, 2)

        self.render(count, count_1, count_2, last_count, context)

    def render(self, count, count_1, count_2, last_count, context):
        context.update({'cur_1': x[1] for x in currency if str(x[0]) == str(count_1)})
        context.update({'cur_2': x[1] for x in currency if str(x[0]) == str(count_2)})

        context.update(
            {
                'count': count,
                'count_1': count_1,
                'count_2': count_2,
                'last_count': last_count,
            }
        )
