class Player:
    def __init__(self, unique_id: str, player_name: str):
        """
        Initialize a Player Object

        :param unique_id: Unique ID of the player
        :param player_name: Name of the player
        """
        self.unique_id = unique_id
        self.player_name = player_name

    @property
    def uid(self):
        return self.unique_id

    @property
    def name(self):
        return self.player_name

    def __str__(self) -> str:
        return f"Player's name is {self.name} and ID: {self.uid}"