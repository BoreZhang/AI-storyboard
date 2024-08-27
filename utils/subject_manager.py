class SubjectManager:
    def __init__(self):
        self.subjects = {}
        self.current_scene = None

    def add_subject(self, name, description, image_embedding=None):
        self.subjects[name] = {
            "description": description,
            "image_embedding": image_embedding,
            "components": {}
        }

    def add_component(self, subject_name, component_name, description):
        self.subjects[subject_name]["components"][component_name] = description

    def set_scene(self, scene_description):
        self.current_scene = scene_description

    def get_context(self):
        context = f"Scene: {self.current_scene}\n"
        for name, subject in self.subjects.items():
            context += f"{name}: {subject['description']}\n"
            for comp_name, comp_desc in subject['components'].items():
                context += f"  - {comp_name}: {comp_desc}\n"
        return context