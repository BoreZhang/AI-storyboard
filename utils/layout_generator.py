from utils.llm_integration import LLMIntegration

class LayoutGenerator:
    def __init__(self):
        self.llm = LLMIntegration()

    def generate_layout(self, context, image_size):
        prompt = f"Given the following context and image size {image_size}, generate bounding boxes for each subject and component:\n{context}\nFormat: [subject_name, x1, y1, x2, y2]"
        response = self.llm.generate(prompt)
        return self.parse_layout(response)

    def parse_layout(self, layout_text):
        layout = {}
        for line in layout_text.split('\n'):
            if line.strip():
                subject, x1, y1, x2, y2 = eval(line)
                layout[subject] = [float(x1), float(y1), float(x2), float(y2)]
        return layout