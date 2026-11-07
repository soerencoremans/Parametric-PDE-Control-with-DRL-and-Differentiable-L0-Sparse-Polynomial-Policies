import torch

actor = torch.load("saved_models/poly_td3_l0seed_1/poly_td3_l0_last_actor_poly.pth")
print(type(actor))
