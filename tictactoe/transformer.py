class transformer:

    rotations = [0, 0, 1, 3, 0, 1, 3, 2, 2]
    diag_ref_trans = [0, 3, 6, 1, 4, 7, 2, 5, 8]
    vert_ref_trans = [2, 1, 0, 5, 4, 3, 8, 7, 6]
    rot_trans = [6, 3, 0, 7, 4, 1, 8, 5, 2]


    def __init__(self, move):
        self.first_move = 4 if move == 4 else move % 2
        self.rotation = self.get_rotation(move)
        self.reflection = 0

    def get_rotation(self, move):
        return self.rotations[move]


    def set_reflection(self, move):
        if self.first_move == 4:
            self.rotation = self.rotations[move]
        elif self.first_move == 0:
            self.reflection = 1 if move in [3, 6, 7] else 0 
        elif self.first_move == 1:
            self.reflection = 2 if move in [2, 5, 8] else 0

    @staticmethod
    def transform_board(transformation, board):
        transformed = [board[transformation[i]] for i in range(9)]
        return ''.join(transformed)

    @staticmethod
    def transform_move(transformation, move):
        return transformation[move]

    def rotate(self, move):
        for _ in range(self.rotation):
            move = self.transform_move(self.rot_trans, move)
        return move


    def reflect(self, move):
        if self.reflection == 1:
            move = self.transform_move(self.diag_ref_trans, move)
        elif self.reflection == 2:
            move = self.transform_move(self.vert_ref_trans, move)
        return move


    def transform(self, move):
        return self.reflect(self.rotate(move))

    def undo_transformation(self, board):
        if self.reflection == 1:
            board = self.transform_board(self.diag_ref_trans, board)
        elif self.reflection == 2:
            board = self.transform_board(self.vert_ref_trans, board)
        for _ in range(self.rotation):
            board = self.transform_board(self.rot_trans, board)
        return board
