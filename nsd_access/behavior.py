import pandas as pd

from . import utils as ut


class behavior_handler:
    """ Class to handle behavior files of NSD data
    """

    def __init__(self, behavior_string):
        """ Behavior files handler

        Parameters
        ----------
        behavior_string: str
            String to access behavior files, will be formatted to access each subject

        """
        self.behavior_string = behavior_string

    def read_behavior_file(self, subject, session_index=None, trial_index=None):
        """Returns the behavior dataframe of the subject.

        Parameters
        ----------
        subject : str or int
            subject identifier
        session_index : int, optional
            which session counting from 0, by default returns all sessions
        trial_index : list, optional
           which trials from this session's behavior to return, by default returns all trials

        Returns
        -------
        pandas DataFrame
            DataFrame containing the behavioral information for the requested trials
        """
        subject = ut.subject_identifier(subject)
        behavior = pd.read_csv(
            self.behavior_string.format(subject=subject),
            delimiter='\t'
        )

        # the behavior is encoded per run.
        # I'm now setting this function up so that it aligns with the timepoints in the fmri files,
        # i.e. using indexing per session, and not using the 'run' information.
        if session_index:
            behavior = behavior[behavior['SESSION'] == session_index]
        if trial_index:
            return behavior.iloc[trial_index]
        return behavior

    def get_repeated_conditions(self, subject, n_repeat=3):
        """
        Creates a dictionary of the session, trial of the images that were seen n_repeat times by the subject
        Args:
            subject (int or str): identifier of the subject between
            n_repeat (int): the number of times to be seen to be considered valid
        Returns:
            repeated_images (list): List of the 73KID images that were seen n_repeat times
        """
        behavior = self.read_behavior_file(subject)
        result = behavior['73KID'].value_counts()[behavior['73KID'].value_counts() >= n_repeat].index.tolist()
        return result

    def get_515_index(self):
        """
        Return the index of the 515 images that where seen by all subject.
        Returns:
            List: list of 73KID of the 515 images 
        """
        # Load the repeated_conditions of each subject.
        # Merge them
        # return as list

