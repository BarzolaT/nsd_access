"""
Utilitary functions to simplify process of the nsda class
"""


def subject_identifier(subject):
    """Return a valid subject identifier

    Parameters
    ----------
    subject : str or int
        subject identifier or number

    Returns
    ----------
    str
        valid subject identifier in the format 'subjxx'

    Raises
    ----------
    ValueError
        If the string or int cannot be associated with a valid subject of the nsd dataset
    """
    if isinstance(subject, str):
        if (
            len(subject) == 6 and
            subject.startswith("subj0") and
            subject[-1].isdigit() and
            int(subject[-1]) < 9 and
            int(subject[-1]) > 0
        ):
            return subject
        else:
            raise ValueError(f"Subject {subject} is not a valid nsd subject")
    elif isinstance(subject, int):
        if subject > 8 or subject < 1:
            raise ValueError(f"Subject number {subject} does not exist")
        return f"subj0{subject}"
