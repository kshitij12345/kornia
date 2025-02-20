import torch
import torch.nn as nn


class Vflip(nn.Module):
    r"""Vertically flip a tensor image or a batch of tensor images. Input must
    be a tensor of shape (C, H, W) or a batch of tensors :math:`(*, C, H, W)`.

    Args:
        input (torch.Tensor): input tensor

    Returns:
        torch.Tensor: The vertically flipped image tensor

    Examples:
        >>> input = torch.tensor([[[
            [0., 0., 0.],
            [0., 0., 0.],
            [0., 1., 1.]]]])
        >>> vflip = kornia.flip(input, -2)
        tensor([[[0, 1, 1],
                 [0, 0, 0],
                 [0, 0, 0]]])
    """

    def __init__(self) -> None:

        super(Vflip, self).__init__()

    def forward(self, input: torch.Tensor) -> torch.Tensor:  # type: ignore
        return vflip(input)

    def __repr__(self):
        return self.__class__.__name__


class Hflip(nn.Module):
    r"""Horizontally flip a tensor image or a batch of tensor images. Input must
    be a tensor of shape (C, H, W) or a batch of tensors :math:`(*, C, H, W)`.

    Args:
        input (torch.Tensor): input tensor

    Returns:
        torch.Tensor: The horizontally flipped image tensor

    Examples:
        >>> input = torch.tensor([[[
            [0., 0., 0.],
            [0., 0., 0.],
            [0., 1., 1.]]]])
        >>> hflip = kornia.flip(input, -1)
        tensor([[[0, 0, 0],
                 [0, 0, 0],
                 [1, 1, 0]]])
    """

    def __init__(self) -> None:

        super(Hflip, self).__init__()

    def forward(self, input: torch.Tensor) -> torch.Tensor:  # type: ignore
        return hflip(input)

    def __repr__(self):
        return self.__class__.__name__


class Rot180(nn.Module):
    r"""Rotate a tensor image or a batch of tensor images
        180 degrees. Input must be a tensor of shape (C, H, W)
        or a batch of tensors :math:`(*, C, H, W)`.

        Args:
            input (torch.Tensor): input tensor

        Examples:
            >>> input = torch.tensor([[[
                [0., 0., 0.],
                [0., 0., 0.],
                [0., 1., 1.]]]])
            >>> rot180 = kornia.rot180(input)
            tensor([[[1, 1, 0],
                    [0, 0, 0],
                    [0, 0, 0]]])
        """

    def __init__(self) -> None:

        super(Rot180, self).__init__()

    def forward(self, input: torch.Tensor) -> torch.Tensor:  # type: ignore
        return rot180(input)

    def __repr__(self):
        return self.__class__.__name__


def rot180(input: torch.Tensor) -> torch.Tensor:

    r"""Rotate a tensor image or a batch of tensor images
    180 degrees. Input must be a tensor of shape (C, H, W)
    or a batch of tensors :math:`(*, C, H, W)`.

    Args:
        input (torch.Tensor): input tensor

    Returns:
        torch.Tensor: The rotated image tensor

    """

    return torch.flip(input, [-2, -1])


def hflip(input: torch.Tensor) -> torch.Tensor:
    r"""Horizontally flip a tensor image or a batch of tensor images. Input must
    be a tensor of shape (C, H, W) or a batch of tensors :math:`(*, C, H, W)`.

    Args:
        input (torch.Tensor): input tensor

    Returns:
        torch.Tensor: The horizontally flipped image tensor

    """

    return torch.flip(input, [-1])


def vflip(input: torch.Tensor) -> torch.Tensor:
    r"""Vertically flip a tensor image or a batch of tensor images. Input must
    be a tensor of shape (C, H, W) or a batch of tensors :math:`(*, C, H, W)`.

    Args:
        input (torch.Tensor): input tensor

    Returns:
        torch.Tensor: The vertically flipped image tensor

    """

    return torch.flip(input, [-2])
