import torch

# MACL temperature strategy with reweighing

# pos: positive representation similarities, Nx1
# neg: negative representation similarities, NxK
# tau_0: basic temperature
# alpha: scaling factor
# A0: initial alignment threshold
    
def MACL(pos, neg, tau_0, alpha, A0):
    
    # alignment-adaptive temperature
    A=torch.mean(pos.detach())
    tau = tau_0 * (1. + alpha*(A-A0))
    
    logits = torch.cat([pos, neg], dim=1) / tau  
    P = torch.softmax(logits, dim=1)[:,0]
    
    # reweighting and loss computation
    V = 1. / (1.- P)
    loss = -V.detach() * torch.log(P)
    
    return loss.mean()
