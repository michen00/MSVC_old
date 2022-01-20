"""tests for process_audio"""

from msvc.src.features.process_audio import process_audio


class TestProcessAudio(object):
    def test_dataframe(self):
        """checks the returned dataframe"""
        from pandas import DataFrame, read_feather
        from pydub import AudioSegment
        import tensorflow.compat.v2 as tf
        import tensorflow_hub as hub

        tf.enable_v2_behavior()

        class mock_session:
            audio_buffer = AudioSegment.from_wav("tests/features/test.wav")

        test_audio = process_audio(
            mock_session,
            hub.load("https://tfhub.dev/google/nonsemantic-speech-benchmark/frill/1"),
        )
        assert type(test_audio) == DataFrame
        assert len(test_audio.columns) == 2048
        assert not test_audio.isnull().values.any()
        assert all(test_audio == read_feather("tests/features/test_df.feather"))
