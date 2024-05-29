from django import forms

from django import forms


class SelectionForm(forms.Form):
    MAJOR_CHOICES = [
        ('disabled selected', 'Select a Domain'),
        ('Arts and crafts', 'Arts and Crafts'),
        ('Story time', 'Story Time'),
        ('Science experiments', 'Science Experiments'),
        ('Sports', 'Sports'),
        ('Music', 'Music'),
        ('Nature and environment', 'Nature and Environment'),
        ('Languages', 'Languages'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Computer science', 'Computer Science'),
        ('Business', 'Business Administration'),
        ('Engineering', 'Engineering'),
        ('Biology', 'Biology'),
        ('Psychology', 'Psychology'),
        ('Education', 'Education'),
        ('Art', 'Art and Design'),
        ('Literature', 'Literature'),
        ('Mathematics', 'Mathematics'),
    ]

    CHAPTER_CHOICES = {
        'Arts and crafts': [
            ('Drawing', 'Drawing'),
            ('Painting', 'Painting'),
            ('Origami', 'Origami'),
            ('Clay modeling', 'Clay Modeling'),
            ('Collage', 'Collage'),
        ],
        'Story time': [
            ('Fairy tales', 'Fairy Tales'),
            ('Adventure stories', 'Adventure Stories'),
            ('Animal stories', 'Animal Stories'),
            ('Fantasy', 'Fantasy'),
            ('Bedtime stories', 'Bedtime Stories'),
        ],
        'Science experiments': [
            ('Simple chemistry', 'Simple Chemistry'),
            ('Plant growth', 'Plant Growth'),
            ('magnetism', 'Magnetism'),
            ('Water cycle', 'Water Cycle'),
            ('Volcano eruption', 'Volcano Eruption'),
        ],
        'sports': [
            ('Soccer', 'Soccer'),
            ('Basketball', 'Basketball'),
            ('Swimming', 'Swimming'),
            ('Gymnastics', 'Gymnastics'),
            ('Track and field', 'Track and Field'),
        ],
        'music': [
            ('Singing', 'Singing'),
            ('Playing instruments', 'Playing Instruments'),
            ('Music theory', 'Music Theory'),
            ('Composing', 'Composing'),
            ('Music history', 'Music History'),
        ],
        'Computer science': [
            ('Programming', 'Programming'),
            ('Data_structures', 'Data Structures'),
            ('Algorithms', 'Algorithms'),
            ('Databases', 'Databases'),
            ('Web development', 'Web Development'),
            ('Machine learning', 'Machine Learning'),
            ('Cyber security', 'Cyber Security'),
        ],
        'Business': [
            ('Accounting', 'Accounting'),
            ('Marketing', 'Marketing'),
            ('Management', 'Management'),
            ('Finance', 'Finance'),
            ('Entrepreneurship', 'Entrepreneurship'),
            ('Business_ethics', 'Business Ethics'),
            ('Supply_chain', 'Supply Chain Management'),
        ],
        'Engineering': [
            ('Thermodynamics', 'Thermodynamics'),
            ('Circuits', 'Circuits'),
            ('Materials_science', 'Materials Science'),
            ('Fluid_mechanics', 'Fluid Mechanics'),
            ('Mechanics', 'Mechanics'),
            ('Control systems', 'Control Systems'),
            ('Robotics', 'Robotics'),
        ],
        'Biology': [
            ('Genetics', 'Genetics'),
            ('Cell biology', 'Cell Biology'),
            ('Ecology', 'Ecology'),
            ('Evolution', 'Evolution'),
            ('Microbiology', 'Microbiology'),
            ('Anatomy', 'Anatomy'),
            ('Physiology', 'Physiology'),
        ],
        'Psychology': [
            ('Cognitive psychology', 'Cognitive Psychology'),
            ('Developmental psychology', 'Developmental Psychology'),
            ('Clinical psychology', 'Clinical Psychology'),
            ('Social psychology', 'Social Psychology'),
            ('Neuropsychology', 'Neuropsychology'),
            ('Behavioral psychology', 'Behavioral Psychology'),
        ],
        'Education': [
            ('Curriculum design', 'Curriculum Design'),
            ('Educational technology', 'Educational Technology'),
            ('Classroom management', 'Classroom Management'),
            ('Special education', 'Special Education'),
            ('Early childhood education', 'Early Childhood Education'),
            ('Educational psychology', 'Educational Psychology'),
        ],
        'Art': [
            ('Drawing', 'Drawing'),
            ('Painting', 'Painting'),
            ('Sculpture', 'Sculpture'),
            ('Digital_art', 'Digital Art'),
            ('Art_history', 'Art History'),
            ('Graphic_design', 'Graphic Design'),
            ('Photography', 'Photography'),
        ],
        'Literature': [
            ('Classical literature', 'Classical Literature'),
            ('Modern literature', 'Modern Literature'),
            ('Poetry', 'Poetry'),
            ('Drama', 'Drama'),
            ('Literary_criticism', 'Literary Criticism'),
            ('World literature', 'World Literature'),
        ],
        'Mathematics': [
            ('Algebra', 'Algebra'),
            ('Calculus', 'Calculus'),
            ('Geometry', 'Geometry'),
            ('Statistics', 'Statistics'),
            ('Discrete math', 'Discrete Mathematics'),
            ('Linear algebra', 'Linear Algebra'),
            ('Number theory', 'Number Theory'),
        ],
        'Nature and environment': [
            ('Animals', 'Animals'),
            ('Plants', 'Plants'),
            ('Weather', 'Weather'),
            ('Recycling', 'Recycling'),
            ('Conservation', 'Conservation'),
        ],
        'Languages': [
            ('English', 'English'),
            ('Spanish', 'Spanish'),
            ('French', 'French'),
            ('German', 'German'),
            ('Chinese', 'Chinese'),
            ('Japanese', 'Japanese'),
            ('Arabic', 'Arabic'),
            ('Russian', 'Russian'),
            ('Portuguese', 'Portuguese'),
            ('Italian', 'Italian'),
        ],
        'History': [
            ('Ancient history', 'Ancient History'),
            ('Medieval history', 'Medieval History'),
            ('Modern history', 'Modern History'),
            ('World war history', 'World War History'),
            ('History of science', 'History of Science'),
            ('History of art', 'History of Art'),
            ('History of music', 'History of Music'),
        ],
        'Geography': [
        ('World geography', 'World Geography'),
        ('Countries and capitals', 'Countries and Capitals'),
        ('Maps and globes', 'Maps and Globes'),
        ('Oceans and continents', 'Oceans and Continents'),
        ('Climate zones', 'Climate Zones'),
        ('Landforms', 'Landforms'),
        ('Natural disasters', 'Natural Disasters'),
        ('Environmental issues', 'Environmental Issues'),
        ],
    }

    domain = forms.ChoiceField(choices=MAJOR_CHOICES)
    subdomain = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(SelectionForm, self).__init__(*args, **kwargs)
        if 'domain' in self.data:
            domain = self.data.get('domain')
            self.fields['subdomain'].choices = self.CHAPTER_CHOICES.get(domain, [])
        else:
            self.fields['subdomain'].choices = []
