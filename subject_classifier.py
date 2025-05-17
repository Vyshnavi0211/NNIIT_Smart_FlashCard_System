""" 
This module contains the logic to infer the subject of a flashcard based on rule-based keyword matching
"""

def infer_subject(text: str) ->str:
    """
    Infers the subject of the flashboard based on keywords in the question text.
    
    Args:
        text(str): The question(which is a text) from flashcard.

    Returns:
        str: The inferred subject, e.g., "Physics", "Biology"  
    """

    text = text.lower()
    keywords = {
        "Physics": ["force", "acceleration", "velocity", "newton", "gravity", "energy", "momentum"],
        "Biology": ["photosynthesis", "cell", "organism", "plant", "enzyme", "mitochondria", "tissue", "gland"],
        "Chemistry": ["atom", "molecule", "reaction", "acid", "base", "compound", "bond"],
        "Math": ["algebra", "geometry", "equation", "derivative", "integral", "differentiation", "calculus"],
        "History": ["war", "revolution", "empire", "ancient", "medieval", "treaty", "kingdom", "mughal"],
        "Geography": ["continent", "river", "mountain", "ocean", "climate", "desset", "fertile"]
    }

    for subject, terms in keywords.items():
        if any(word in text for word in terms):
            return subject
    return "General"
