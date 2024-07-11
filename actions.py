from scrapers import get_exam_details

class ActionGetExamInfo:
    def get_exam_info(self, exam_name):
        details = get_exam_details(f'https://example.com/{exam_name}-details')
        return {
            "response": f"The {details['exam_name']} exam is scheduled on {details['exam_date']}."
        }
