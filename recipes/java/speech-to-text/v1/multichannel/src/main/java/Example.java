/**
 * Recipe: Multichannel (Speech-to-Text v1)
 * Transcribes each audio channel independently — useful for stereo call recordings.
 * Without multichannel: all channels are mixed into one transcript.
 * With multichannel: separate transcript per channel.
 * See also: diarize for speaker identification in single-channel audio
 */
import DeepgramClient;
import java.util.Collections;
import resources.listen.v1.media.requests.ListenV1RequestUrl;
import resources.listen.v1.media.types.MediaTranscribeRequestModel;
import resources.listen.v1.media.types.MediaTranscribeResponse;
import types.ListenV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        MediaTranscribeResponse result = client.listen().v1().media().transcribeUrl(
            ListenV1RequestUrl.builder()
                .url("https://dpgr.am/spacewalk.wav")
                .model(MediaTranscribeRequestModel.NOVA3)
                .multichannel(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: diarize(true), punctuate(true)
                .build());

        // Path: results.channels[] — one entry per audio channel
        ListenV1Response response = (ListenV1Response) result.get();
        var channels = response.getResults().getChannels();
        for (int i = 0; i < channels.size(); i++) {
            System.out.println("Channel " + i + ":");
            channels.get(i).getAlternatives().orElse(Collections.emptyList())
                .get(0).getTranscript().ifPresent(t -> System.out.println("  " + t));
        }
    }
}