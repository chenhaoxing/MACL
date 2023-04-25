import torch

class MACLa(object):

    def __init__(self, tau_init=0.1, alpha=2.0):
        super(MACLa, self).__init__()
        self.tau_init = tau_init
        self.alpha = alpha

    def __call__(self, fx, gx):
        logits = fx @ gx.T
        A=(torch.trace(logits)/fx.shape[0]).detach()
        tau = self.tau_init * self.alpha**A
        P = torch.softmax(logits/tau, dim=1)

        mask = torch.ones(P.shape, device=fx.device).fill_diagonal_(0).bool()
        W0 = (P.masked_select(mask)).view(P.shape[0],-1).sum(-1)
        W1 = torch.ones(fx.shape[0], device=fx.device)
        W = W1 / W0

        loss = -W.detach() * torch.log(P).diag()
        return loss.mean()


class MACLb(object):

    def __init__(self, tau_init=0.1, beta=1.0):
        super(MACLb, self).__init__()
        self.tau_init = tau_init
        self.beta = beta

    def __call__(self, fx, gx):
        logits = fx @ gx.T
        A=(torch.trace(logits)/fx.shape[0]).detach()
        tau = self.tau_init*(1 + self.beta*A)
        P = torch.softmax(logits/tau, dim=1)

        mask = torch.ones(P.shape, device=fx.device).fill_diagonal_(0).bool()
        W0 = (P.masked_select(mask)).view(P.shape[0],-1).sum(-1)
        W1 = torch.ones(fx.shape[0], device=fx.device)
        W = W1 / W0

        loss = -W.detach() * torch.log(P).diag()
        return loss.mean()
