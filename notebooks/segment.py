def segment_signal(sampling_frequency,duration,signal):

    samples_in_segment=sampling_frequency*duration

    seg_count=len(signal)/samples_in_segment    
    
    segments=[]
    for i in range(seg_count):
        segments.append(signal[i*samples_in_segment:(i+1)*samples_in_segment])

    return seg_count,segments
