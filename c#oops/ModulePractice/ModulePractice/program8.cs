namespace ModulePractice;
public interface Iplayable
{
    void Play();
}
public class MusicPlayer : Iplayable
{
    public void Play()
    {
        Console.WriteLine("Music Player is Playing");
    }
}

public class VideoPlayer : Iplayable
{
    public void Play()
    {
        Console.WriteLine("Video Player is Playing");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Iplayable music = new MusicPlayer();
//         Iplayable video = new VideoPlayer();
//         music.Play();
//         video.Play();
//     }
// }