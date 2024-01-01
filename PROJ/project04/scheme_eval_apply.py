import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        open=scheme_eval(first,env)
        validate_procedure(open)
        if isinstance(open,MacroProcedure):
            temp=scheme_apply(open,rest,env)
            if isinstance(temp,Unevaluated):
                uptemp=scheme_eval(temp.expr,temp.env)
                return Unevaluated(uptemp,env)
            else:
                return scheme_eval(temp,env)
            
        def single_arg_f(operand):
            return scheme_eval(operand,env)
        oprands=rest.map(single_arg_f)
        return scheme_apply(open,oprands,env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        mylst=[]
        while args!=nil:
            mylst.append(args.first)
            args=args.rest
        
        if procedure.expect_env:
            mylst.append(env)
        try:
            return procedure.py_func(*mylst)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        new_env=procedure.env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body,new_env)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        new_env=env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body,new_env)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if expressions == nil:
        return None
    if expressions.rest == nil:
        return scheme_eval(expressions.first, env, True)#change here for EC problem
    else: 
        scheme_eval(expressions.first, env)
        return eval_all(expressions.rest, env)
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env

def optimize_tail_calls(original_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        #Follow the RULES in the website!!!!!
        result = Unevaluated(expr, env)
        while isinstance(result, Unevaluated):
            result = original_scheme_eval(result.expr, result.env)
        return result
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
scheme_eval = optimize_tail_calls(scheme_eval)
