
def probability_of_dominant_phenotype(k, m, n):
    """
    :param k, m, and n: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
    :return:  The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
    """
    prob_dom=dominant_prob(k,m,n)
    prob_het=hetero_prob(k,m,n)
    prob_rec=recessive_prob(k,m,n)
    return prob_dom+prob_het+prob_rec

def dominant_prob(k, m, n):
    """
    calculates probability for when dominant allele is picked first
    """
    total=k+m+n
    pr_x = k/total
    ans = 0
    ans+=(pr_x*((k-1)/(total-1)))
    ans+=pr_x*(m/(total-1))
    ans+=pr_x*(n/(total-1))
    return ans

def hetero_prob(k,m,n):
    """
    calculates probability for when heterozygous allele is picked first
    """
    total=k+m+n
    pr_x = m/total
    ans=0
    ans+=pr_x*(k/(total-1))
    ans+=pr_x*((m-1)/(total-1))*0.75
    ans+=pr_x*(n/(total-1))*0.5
    return ans

def recessive_prob(k,m,n):
    """
    calculates probability for when recessive allele is picked first
    """
    total=k+m+n
    pr_x = n/total
    ans=0
    ans+=pr_x*(k/(total-1))
    ans+=pr_x*(m/(total-1))*0.5
    #no recessive x recessive because it gives a probability of 100% recessive = 0% dominant
    return ans

if __name__ == "__main__":
    ans=probability_of_dominant_phenotype(17.0, 20.0, 23.0)
    print ans